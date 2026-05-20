# Introduction

## What Are We Actually Building?

You've probably heard of ChatGPT. It's impressive — it can write essays, answer questions, explain code. But how does it work?

The honest answer is: it learned to predict text. Given some words, it guesses what word comes next. It does this so well, so fast, across so much knowledge, that the result feels like thinking.

**Slice GPT Lab** is a tiny version of that same idea.

We're not trying to build the next ChatGPT. We're building something small enough to understand completely — a model you can train in minutes on your own computer, then watch it generate answers character by character.

## The Pizzeria Setting

To keep things concrete, we trained the model on a fictional pizzeria called **The Slice Lab**.

The training data is a set of simple English conversations:

```txt
<|user|>
What pizza do you recommend?
<|assistant|>
I recommend the Margherita pizza.
<|end|>
```

The model reads thousands of these characters and learns to continue them. When you ask "What pizza do you recommend?", it generates the answer — not by looking up a hardcoded string, but by predicting one character at a time.

## What You Should Pay Attention To

When you run training, you'll see a number called **loss** printed each step:

```txt
step=10  loss=3.1204
step=20  loss=2.6870
step=30  loss=2.4103
```

Loss going down = the model is getting better at predicting characters from this dataset.

But here's the important part: **lower loss does not mean the model became smart.** It means it got better at repeating patterns from a tiny dataset. ChatGPT's quality comes from training on billions of examples for weeks. Our model trains for minutes. That gap matters.

The point of this project is to understand the *mechanics*, not to produce impressive outputs.

## The Invisible Steps

When you send a question to ChatGPT, a lot happens in milliseconds. This project makes those steps visible:

- Text becomes numbers (tokenization)
- Numbers become vectors (embeddings)
- Vectors pick up position information
- Attention connects each word to earlier words
- A score is produced for every possible next word (logits)
- The model picks one word and repeats
- The answer arrives character by character

By the end of this course, you'll understand every one of these steps.

<!-- COURSE_THREAD_START -->
## Course Thread

Previous: [Course Guide](00_course_guide.md) sets the route and commands.

Next: [How LLMs Work](02_how_llms_work.md) zooms out to the full GPT-like flow.

<!-- COURSE_THREAD_END -->
