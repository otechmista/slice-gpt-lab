# How LLMs Work

LLM stands for **Large Language Model**. ChatGPT, Gemini, Claude — they're all LLMs. Despite the fancy name, they all learned one humble skill:

> **Given the previous words, predict the next word.**

That's it. No secret magic. Just that task, done millions of times, on enormous amounts of text.

## A Simple Analogy

Imagine you're texting with a friend who finishes your sentences. You type:

```txt
I'd like a large Margherita pi...
```

Your friend guesses "pizza" because they've seen you say this before. An LLM does the same thing — but it has "seen" billions of sentences and learned all sorts of patterns from them.

## The Training Pipeline

Here's what happens when the model learns:

```txt
text from dataset
  → split into tokens (characters, in our case)
  → convert tokens to IDs (numbers)
  → group into batches
  → transform into embeddings (number vectors)
  → add position information
  → run through transformer blocks (attention + thinking)
  → produce a score for every possible next token (logits)
  → compare to the real next token → calculate the loss (how wrong was the guess?)
  → backpropagation → adjust the weights slightly
  → repeat thousands of times
```

Each step of this pipeline has its own file in this project. You'll understand all of them.

## The Inference Pipeline

When the model answers a question, there's no more learning — just predicting:

```txt
your prompt
  → convert to token IDs
  → run through the model
  → produce scores for the next token
  → pick one token (based on those scores)
  → add it to the prompt
  → repeat until done
```

The model generates one character at a time, feeding each result back into itself. That's called **autoregressive** generation.

## What Are Logits?

When the model processes a sequence, it produces a number for every possible next character. These numbers are called **logits**.

Our model knows 54 different characters. So after reading "What piz", it produces 54 scores like:

```txt
'z' → 8.2   (high! makes sense after "piz")
'a' → 3.1
'x' → 0.1   (very unlikely)
...
```

These scores get turned into probabilities, and the model picks one character. That character is added to the sequence, and the process repeats.

## Why the Output Can Be Strange

Our model is tiny. It was trained for a few minutes on a small dataset. Real LLMs are trained for weeks on billions of examples, on racks of specialized hardware.

If our model produces weird text, that's not a bug — it's the lesson. **Architecture alone doesn't create quality.** Scale, data, and training time matter enormously.

To get better output from this model, you could:

- Add more training examples to `app/dataset.txt`
- Train for more steps
- Make the model bigger
- Lower the temperature (makes output less random)

But the goal here isn't impressive output. It's understanding how the machine works.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Introduction](01_introduction.md) introduces the project and pizzeria domain.

Next: [Simple Context Model](15_simple_context_model.md) shows how chat messages become model input.

<!-- COURSE_THREAD_END -->
