# Slice GPT Lab

## A hands-on course for understanding how GPT-style language models work

---

Have you ever wondered how ChatGPT actually generates text? Not the marketing explanation — the real one?

This project shows you. Step by step, in real code you can run, modify, and break on purpose.

**Slice GPT Lab** is a tiny AI trained to talk about a fictional pizzeria called The Slice Lab. The pizzeria is just a prop to keep things concrete. The real subject is the model: how it reads text, learns from it, and generates answers one character at a time — the same way every major language model works, at a scale small enough to understand completely.

This is not a product. It is a classroom.

---

## Who This Is For

Anyone curious about how AI language models work. No machine learning background required — just curiosity and willingness to run some Python.

If you've ever asked "how does ChatGPT produce text?", this project gives you the real answer.

---

## What You'll Be Able to Explain After This

By the end of the course, you'll understand every step in this chain:

```
your question
  → split into characters (tokenization)
  → each character becomes a number (token IDs)
  → numbers become vectors (embeddings)
  → position is added to each vector
  → tokens look at each other (attention)
  → each token transforms its own info (feed-forward)
  → a score is produced for every possible next character (logits)
  → one character is picked
  → it's added to the sequence
  → repeat until the answer is done
```

You'll also understand how the model learned to do all of that in the first place — from a simple training loop that runs on your laptop in minutes.

---

## How to Set Up

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python app/train.py
```

Ask it a question:

```bash
python app/infer.py --prompt "What pizza do you recommend?"
```

Start the web API:

```bash
uvicorn app.api:app --reload
```

Run all tests:

```bash
python -m pytest
```

---

## The Book

This course is structured as a sequence of lessons, each building on the last. Start at the top and follow the thread.

### Part 0: Orientation

| | Document | What You'll Learn |
|---|---|---|
| 1 | [00_course_guide.md](00_course_guide.md) | Commands, study order, and the key idea |
| 2 | [01_introduction.md](01_introduction.md) | What we're building and why |

### Part 1: The Big Picture

| | Document | What You'll Learn |
|---|---|---|
| 3 | [02_how_llms_work.md](02_how_llms_work.md) | The full GPT-like pipeline, from text to prediction |
| 4 | [15_simple_context_model.md](15_simple_context_model.md) | How a chat conversation becomes model input |

### Part 2: Inside the Model

| | Document | What You'll Learn |
|---|---|---|
| 5 | [03_tokenization.md](03_tokenization.md) | How text becomes numbers |
| 6 | [04_embeddings.md](04_embeddings.md) | How numbers become vectors with meaning |
| 7 | [05_self_attention.md](05_self_attention.md) | How tokens look back at previous context |
| 8 | [06_transformer_blocks.md](06_transformer_blocks.md) | Attention + feed-forward, the repeating unit |
| 9 | [07_forward_pass.md](07_forward_pass.md) | How the model produces a prediction |

### Part 3: Learning

| | Document | What You'll Learn |
|---|---|---|
| 10 | [08_loss_and_backpropagation.md](08_loss_and_backpropagation.md) | How the model measures and learns from mistakes |
| 11 | [09_training_loop.md](09_training_loop.md) | The complete training process |
| 12 | [11_checkpoint_and_weights.md](11_checkpoint_and_weights.md) | How trained knowledge is saved to disk |

### Part 4: Using the Model

| | Document | What You'll Learn |
|---|---|---|
| 13 | [10_inference.md](10_inference.md) | How the model generates answers, one character at a time |
| 14 | [12_openai_api_layer.md](12_openai_api_layer.md) | How to expose the model as a web API |
| 15 | [13_limitations_of_the_model.md](13_limitations_of_the_model.md) | Why this isn't ChatGPT, and what that means |

### Part 5: The Code

| | Document | What You'll Learn |
|---|---|---|
| 16 | [14_file_by_file_lessons.md](14_file_by_file_lessons.md) | Every source file explained with questions to answer |

---

## Visual Diagrams

If you prefer to see the flows visually:

```
docs/diagrams/README.md
```

---

## Architecture Views

For deeper context on design decisions (read these before changing the structure):

```
docs/contexts/01_CONTEXT_VIEW.md   ← problem, goals, and boundaries
docs/contexts/02_CONTAINER_VIEW.md ← runtime components
docs/contexts/03_COMPONENT_VIEW.md ← internal structure
docs/contexts/04_CODE_VIEW.md      ← contracts and rules
```

---

## The Core Idea

The model learns one skill, repeated thousands of times:

> Given the previous characters, predict the next character.

That same idea powers every GPT-style model — ChatGPT, Claude, Gemini. Here it's small enough to see clearly.
