# Course Guide

Welcome to **Slice GPT Lab** — a hands-on mini classroom where you'll build and understand a tiny version of the same technology behind ChatGPT.

You won't just read about AI. You'll train a real model, watch it learn, and talk to it.

## What This Project Does

There is a fictional pizzeria called **The Slice Lab**. We trained a small AI on pizza conversations. When you ask it "What pizza do you recommend?", the model generates the answer character by character — just like a real language model does. No cheating, no hardcoded answers.

## How to Study

Follow this order. Each step builds on the last:

1. Read this guide (you're here).
2. [01_introduction.md](01_introduction.md) — what we're building and why.
3. [02_how_llms_work.md](02_how_llms_work.md) — the big picture of how AI language models work.
4. [15_simple_context_model.md](15_simple_context_model.md) — how a conversation becomes model input.
5. [03_tokenization.md](03_tokenization.md) through [13_limitations_of_the_model.md](13_limitations_of_the_model.md) — one concept at a time.
6. [14_file_by_file_lessons.md](14_file_by_file_lessons.md) — connect every concept back to real code.
7. Open the files in `app/` and explore.
8. Run the tests, train the model, ask it questions.

## Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python app/train.py
```

Ask the trained model a pizza question:

```bash
python app/infer.py --prompt "What pizza do you recommend?"
```

Ask it something it wasn't trained on:

```bash
python app/infer.py --prompt "What is the capital of France?"
```

See the full raw generated conversation:

```bash
python app/infer.py --raw-model --prompt "What pizza do you recommend?"
```

Start the API server:

```bash
uvicorn app.api:app --reload
```

Run all tests:

```bash
python -m pytest
```

## The Files and What They Teach

| File | What you'll learn |
|---|---|
| `app/dataset.txt` | The training examples — the pizzeria conversations |
| `app/dataset.py` | How the model loads its training material |
| `app/context.py` | How a chat conversation becomes a single text the model reads |
| `app/tokenizer.py` | How text becomes numbers |
| `app/batch.py` | How training examples are created from text |
| `app/embedding.py` | How numbers become learned vectors |
| `app/position.py` | How the model knows word order |
| `app/attention.py` | How the model pays attention to previous words |
| `app/feedforward.py` | The thinking layer inside each transformer block |
| `app/block.py` | One full transformer block (attention + thinking) |
| `app/model.py` | The whole model — all pieces together |
| `app/loss.py` | How the model measures its own mistakes |
| `app/sampling.py` | How the model picks the next character |
| `app/checkpoint.py` | How trained knowledge is saved and reloaded |
| `app/train.py` | The training loop — where learning actually happens |
| `app/infer.py` | How the model generates answers |
| `app/api.py` | The web API — talk to the model over HTTP |
| `app/schemas.py` | The shapes of API requests and responses |

## The Core Idea

The model learns one simple skill, over and over:

```txt
Given the previous characters, predict the next character.
```

Training example:

```txt
input:  <|user|> What piz
target: |user|> What pizz
```

The target is just the input shifted one character to the right. This simple trick is the same idea behind every GPT-style model — just at a tiny scale.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Course Index](README.md) is the entry point for the course.

Next: [Introduction](01_introduction.md) explains what the project is trying to teach.

<!-- COURSE_THREAD_END -->
