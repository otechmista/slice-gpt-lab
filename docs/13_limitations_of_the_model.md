# Limitations: Why This Isn't ChatGPT

Slice GPT Lab is not a product. It's a study project. Understanding what it *can't* do is just as important as understanding what it can.

## What This Model Can't Do

- Answer reliably about topics not in the training data
- Handle long conversations (64-character context window is tiny)
- Use emoji or non-English characters (not in the vocabulary)
- Produce fluent, consistent text (the model is too small)
- Understand the world in any meaningful sense
- Call APIs, search the web, or remember past sessions

## Why It Doesn't Sound Like ChatGPT

The gap isn't a bug — it's a scale difference:

| Factor | Slice GPT Lab | ChatGPT-like models |
|---|---|---|
| Parameters | ~tens of thousands | billions |
| Training data | ~4,000 characters | hundreds of billions of tokens |
| Training time | minutes, on a laptop | weeks, on thousands of GPUs |
| Tokens | characters | subword pieces |
| Context window | 64 characters | thousands of tokens |
| Instruction tuning | none | extensive |

ChatGPT quality comes from an enormous amount of work at every level: data collection, filtering, model design, training infrastructure, instruction tuning (teaching the model to follow instructions), safety systems, and production-grade inference.

This project implements **the core mechanics**. Those mechanics are real — the same architecture, the same training idea, the same inference loop. But quality requires scale.

## Why There Are No Hardcoded Answers

It might be tempting to make `app/infer.py` check "if the user asks about pizza, return this string." But that would defeat the purpose.

This is a model study. If the model's output is weak, the right response is to understand *why* and improve model-related things:

- More diverse training examples
- More training steps
- Bigger model (more layers, wider embeddings)
- Lower temperature for more consistent output
- Better prompt format matching the training data

Hardcoding answers would hide the model's actual behavior. We want to see it honestly.

## The Real Lesson

The architecture of GPT-style models is learnable. The mechanics — tokenization, embeddings, attention, loss, backpropagation, inference — are all visible in this small codebase.

What you build here is a foundation. Everything in ChatGPT, Claude, Gemini, and Llama is an extension of these same ideas, just at a larger scale.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [OpenAI API Layer](12_openai_api_layer.md) wraps inference in an OpenAI-style endpoint.

Next: [File-by-File Lessons](14_file_by_file_lessons.md) returns to the code and studies each file in detail.

<!-- COURSE_THREAD_END -->
